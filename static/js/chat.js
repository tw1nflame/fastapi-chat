

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

        let author = document.createElement('span');
        author.className = 'author';
        let text = document.createElement('span');
        text.className = 'text';

        author.innerText = data.first_name + ' ' + data.last_name + ': '; 

        let link = document.createElement('a');
        link.href = `/profile/${data.id}`;
        link.appendChild(author);

        text.innerText = data.message;

        message.appendChild(link);
        message.appendChild(text);

    }
    else if (data.type == "new_user") {
        let info = document.createElement('span')
        info.className = "server_info"

        let link = document.createElement('a')
        info.appendChild(link)

        link.innerText = data.first_name + ' ' + data.last_name;
        link.href = `/profile/${data.id}`
        let textBefore = document.createTextNode("Пользователь ");
        let textAfter = document.createTextNode(" подключился к чату");
        message.appendChild(textBefore)
        message.appendChild(info)
        message.appendChild(textAfter)
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