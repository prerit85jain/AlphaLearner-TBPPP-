const canvas = document.getElementById("drawingCanvas");
const ctx = canvas.getContext("2d");
const message = document.getElementById("message");

let drawing = false;
let lastX = 0;
let lastY = 0;


canvas.addEventListener("mousedown", (e) => {
    drawing = true;
    lastX = e.offsetX;
    lastY = e.offsetY;
});

canvas.addEventListener("mouseup", () => drawing = false);

canvas.addEventListener("mousemove", draw);

function draw(e) {
    if (!drawing) return;

    ctx.lineWidth = 4;
    ctx.lineCap = "round";
    ctx.strokeStyle = "black";

    ctx.beginPath();
    ctx.moveTo(lastX, lastY); 
    ctx.lineTo(e.offsetX, e.offsetY); 
    ctx.stroke();

    lastX = e.offsetX; 
    lastY = e.offsetY;
}

document.getElementById("clearCanvas").addEventListener("click", () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
});