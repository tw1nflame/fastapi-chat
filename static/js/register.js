document.getElementById('register-form').addEventListener('submit', async (event) => {


    event.preventDefault();
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;
    const first_name = document.getElementById('register-first-name').value;
    const last_name = document.getElementById('register-last-name').value;



    try {
        const response = await fetch('/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', // Установка правильного Content-Type
            },
            body: JSON.stringify({email, password, first_name, last_name}),
        });
document.getElementById('register-form').addEventListener('submit', async (event) => {


    event.preventDefault();
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;
    const first_name = document.getElementById('register-first-name').value;
    const last_name = document.getElementById('register-last-name').value;



    try {
        const response = await fetch('/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', // Установка правильного Content-Type
            },
            body: JSON.stringify({email, password, first_name, last_name}),
        });

        const result = await response.json();
        if (response.ok) {
            document.getElementById('register-message').innerText = 'Регистрация прошла успешно';
        } else {
            document.getElementById('register-message').innerText = `Error: ${JSON.stringify(result)}`;
        }
    } catch (error) {
        document.getElementById('register-message').innerText = `An error occurred: ${error.message}`;
    }
});
        const result = await response.json();
        if (response.ok) {
            document.getElementById('register-message').innerText = 'Login successful!';
        } else {
            document.getElementById('register-message').innerText = `Error: ${JSON.stringify(result)}`;
        }
    } catch (error) {
        document.getElementById('register-message').innerText = `An error occurred: ${error.message}`;
    }
});