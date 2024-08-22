document.getElementById('logout-link').addEventListener("click", async (event) => {
    event.preventDefault();
    try {
        const response = await fetch('/auth/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded', // Установка правильного Content-Type
            },
        });
        if (response.status == 204) {
            window.location.href = '/auth/login';
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
})