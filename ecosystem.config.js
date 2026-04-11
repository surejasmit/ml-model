// ecosystem.config.js
module.exports = {
  apps: [
    {
      name: "ml-api",
      script: "docker",
      args: "run -p 8000:8000 ml-app",
      autorestart: true
    }
  ]
}