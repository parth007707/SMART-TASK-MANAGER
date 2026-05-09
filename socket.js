const socket = io();

socket.on('connect', () => {
    console.log("Connected");
});

socket.on('notification', (data) => {
    alert(data.message);
});
