document.getElementById('login-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const username = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    const formData = new URLSearchParams();
    formData.append('username', username);
    formData.append('password', password);


    try {
        const response = await fetch('/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded', // Установка правильного Content-Type
            },
            body: formData.toString(),
        });
        if (response.status == 204) {
            window.location.href = '/';
        }
        else{
            const result = await response.json();
            if (response.ok) {
                document.getElementById('login-message').innerText = 'Вход успешен!';

                window.location.href = '/';
            } else {
                document.getElementById('login-message').innerText = `Неправильный логин или пароль`;
            }
        }
    } catch (error) {
        document.getElementById('login-message').innerText = `An error occurred: ${error.message}`;
    }
});