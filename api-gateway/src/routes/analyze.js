const fs = require("fs");
const path = require("path");
const os = require("os");
const { randomUUID } = require("crypto");
const { spawn } = require("child_process");

async function saveUploadedFile(filePart) {
  const uploadsDir = path.join(os.tmpdir(), "media-auth-uploads");
  if (!fs.existsSync(uploadsDir)) {
    fs.mkdirSync(uploadsDir, { recursive: true });
  }

  const requestId = randomUUID();
  const filePath = path.join(uploadsDir, `${requestId}-${filePart.filename}`);

  await new Promise((resolve, reject) => {
    const writeStream = fs.createWriteStream(filePath);

    filePart.file.pipe(writeStream);

    writeStream.on("finish", resolve);
    writeStream.on("error", reject);
    filePart.file.on("error", reject);
  });

  return {
    requestId,
    filePath,
    filename: filePart.filename,
    mimetype: filePart.mimetype,
  };
}

async function analyzeWithPython(payload) {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn("../ai-orchestrator/.venv/bin/python", ["main.py"], {
      cwd: path.join(__dirname, "../../../ai-orchestrator"),
    });

    let stdout = "";
    let stderr = "";

    pythonProcess.stdout.on("data", (data) => {
      stdout += data.toString();
    });

    pythonProcess.stderr.on("data", (data) => {
      stderr += data.toString();
    });

    pythonProcess.on("close", (code) => {
      if (code !== 0) {
        return reject(new Error(stderr || "Python process failed"));
      }

      try {
        resolve(JSON.parse(stdout));
      } catch (err) {
        reject(new Error("Invalid JSON from Python orchestrator"));
      }
    });

    pythonProcess.stdin.write(JSON.stringify(payload));
    pythonProcess.stdin.end();
  });
}

async function routes(fastify) {
  fastify.post("/image", async (request, reply) => {
  const parts = request.parts();

  let claim = null;
  let savedFile = null;

  for await (const part of parts) {
    if (part.type === "field" && part.fieldname === "claim") {
      claim = part.value;
    }

    if (part.type === "file" && part.fieldname === "file") {
      const allowedTypes = ["image/jpeg", "image/png", "image/webp"];

      if (!allowedTypes.includes(part.mimetype)) {
        return reply.code(400).send({ error: "Unsupported image type" });
      }

      savedFile = await saveUploadedFile(part);
    }
  }

  if (!savedFile) {
    return reply.code(400).send({ error: "No file uploaded" });
  }

  const result = await analyzeWithPython({
    request_id: savedFile.requestId,
    file_path: savedFile.filePath,
    filename: savedFile.filename,
    media_type: "image",
    mimetype: savedFile.mimetype,
    claim,
  });

  return result;
});

  fastify.post("/audio", async (request, reply) => {
    const file = await request.file();

    if (!file) {
      return reply.code(400).send({ error: "No file uploaded" });
    }

    const allowedTypes = ["audio/mpeg", "audio/wav", "audio/x-wav", "audio/flac"];
    if (!allowedTypes.includes(file.mimetype)) {
      return reply.code(400).send({ error: "Unsupported audio type" });
    }

    const saved = await saveUploadedFile(file);

    const result = await analyzeWithPython({
      request_id: saved.requestId,
      file_path: saved.filePath,
      filename: saved.filename,
      media_type: "audio",
      mimetype: saved.mimetype,
    });

    return result;
  });
}

module.exports = routes;