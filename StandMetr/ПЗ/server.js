const express = require('express');
const app = express();
const port = 3000;

// Встановлення статичної папки для HTML, CSS, і JavaScript файлів
app.use(express.static('public'));

// Старт сервера
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
