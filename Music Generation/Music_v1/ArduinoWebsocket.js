const ws = new WebSocket('ws://arduino_ip_address:81');

ws.onmessage = function(event) {
    const note = event.data;
    console.log('Received note:', note);
    // 使用 Magenta.js 模型补全旋律
};
