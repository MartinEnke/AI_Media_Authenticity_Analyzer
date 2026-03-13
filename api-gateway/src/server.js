const fastify = require("fastify")({ logger: true });
const cors = require("@fastify/cors");
const multipart = require("@fastify/multipart");

const analyzeRoutes = require("./routes/analyze");

async function startServer() {
  await fastify.register(cors, { origin: true });
  await fastify.register(multipart, {
    limits: {
      fileSize: 20 * 1024 * 1024, // 20 MB
    },
  });

  fastify.get("/health", async () => {
    return { status: "ok", service: "api-gateway" };
  });

  await fastify.register(analyzeRoutes, { prefix: "/analyze" });

  try {
    await fastify.listen({ port: 3000, host: "0.0.0.0" });
    console.log("API Gateway running on http://localhost:3000");
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
}

startServer();