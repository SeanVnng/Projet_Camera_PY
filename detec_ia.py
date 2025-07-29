import http.server
import socketserver

PORT = 8000

html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Détection COCO-SSD (Objets courants)</title>
  <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
  <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd"></script>
    <style>
    body { font-family: sans-serif; text-align: center; background: #f5f5f5; }
    video, canvas { position: absolute; top: 70px; left: 50%; transform: translateX(-50%); }
    h1 { margin-top: 10px; }
    canvas { pointer-events: none; }
  </style>
</head>
<body>
  <h1>Détection d'Objets avec COCO-SSD</h1>
  <video id="webcam" width="640" height="480" autoplay muted playsinline></video>
  <canvas id="canvas" width="640" height="480"></canvas>

  <script>
    let video = document.getElementById("webcam");
    let canvas = document.getElementById("canvas");
    let ctx = canvas.getContext("2d");
    let model;

    async function init() {
      model = await cocoSsd.load();
      console.log("Modèle COCO-SSD chargé");

      const stream = await navigator.mediaDevices.getUserMedia({ video: { width: 640, height: 480 } });
      video.srcObject = stream;

      video.addEventListener("loadeddata", () => {
        detectFrame();
      });
    }

    async function detectFrame() {
      const predictions = await model.detect(video);
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      predictions.forEach(pred => {
        if (pred.score > 0.5) {
          const [x, y, width, height] = pred.bbox;
          ctx.strokeStyle = "red";
          ctx.lineWidth = 2;
          ctx.strokeRect(x, y, width, height);
          ctx.fillStyle = "red";
          ctx.font = "16px Arial";
          ctx.fillText(pred.class + " (" + Math.round(pred.score * 100) + "%)", x, y > 20 ? y - 5 : y + 15);
        }
      });

      requestAnimationFrame(detectFrame);
    }

    init();
  </script>
</body>
</html>
"""

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ['/', '/index.html']:
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serveur actif sur http://localhost:{PORT}")
    httpd.serve_forever()