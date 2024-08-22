

function getCookie(name) {
    let value = `; ${document.cookie}`;
    let parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// Получите токен из cookie
let token = getCookie('auth');


// Установите WebSocket соединение с передачей токена в URL
let ws = new WebSocket(`ws://localhost:8000/ws?token=${token}`);
ws.onmessage = function(event) {
    let data = JSON.parse(event.data);
        
    let chat = document.getElementById('chat-messages');
    let message = document.createElement('div');
    message.className = 'chat-message';

    if (data.type == "message") {

        // Создаем элементы для автора и текста сообщения
        let author = document.createElement('span');
        author.className = 'author';
        let text = document.createElement('span');
        text.className = 'text';

        // Устанавливаем текст для каждого элемента
        author.innerText = data.first_name + ' ' + data.last_name + ': ';
        text.innerText = data.message;

        // Добавляем элементы в сообщение
        message.appendChild(author);
        message.appendChild(text);

        // Добавляем сообщение в чат
    }
    else if (data.type == "info") {
        let info = document.createElement('span')
        info.className = "server_info"
        info.innerText = data.info
        message.appendChild(info)
    }
    
    chat.appendChild(message);


    // Прокручиваем чат до конца
    chat.scrollTop = chat.scrollHeight;

};
function sendMessage(event) {
    event.preventDefault()
    let input = document.getElementById("chat-input")
    if (input.value) {
        ws.send(input.value)
        input.value = ''
    }
}

chat_form = document.getElementById('chat-form')
chat_form.addEventListener('submit', sendMessage)