const fastify = require("fastify")({ logger: true });
const cors = require("@fastify/cors");
const multipart = require("@fastify/multipart");

const analyzeRoutes = require("./routes/analyze");

async function startServer() {
  await fastify.register(cors, {
    origin: ["http://localhost:3001"],
  });

  await fastify.register(multipart, {
    limits: {
      fileSize: 20 * 1024 * 1024,
    },
  });

  fastify.register(analyzeRoutes, {
    prefix: "/analyze",
  });

  fastify.get("/health", async () => {
    return { status: "ok" };
  });

  await fastify.listen({ port: 3000 });
}

startServer();