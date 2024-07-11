<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Banca della Campania Luigi Vantivitelli - Accesso/Registrazione</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="header">
        <h1>Banca della Campania Luigi Vantivitelli</h1>
    </div>
    <div class="container">
        <div class="form-wrapper">
            <div class="tabs">
                <button class="tab-button active" onclick="showTab('login')">Accesso</button>
                <button class="tab-button" onclick="showTab('register')">Registrazione</button>
            </div>
            <div id="login" class="tab-content active">
                <form method="post" action="login.php">
                    <label for="login-username">Username:</label>
                    <input type="text" id="login-username" name="username" required>
                    <label for="login-password">Password:</label>
                    <input type="password" id="login-password" name="password" required>
                    <button type="submit">Accedi</button>
                </form>
            </div>
            <div id="register" class="tab-content">
                <form method="post" action="register.php">
                    <label for="register-username">Username:</label>
                    <input type="text" id="register-username" name="username" required>
                    <label for="register-password">Password:</label>
                    <input type="password" id="register-password" name="password" required>
                    <button type="submit">Registrati</button>
                </form>
            </div>
        </div>
    </div>
    <script>
        function showTab(tabId) {
            document.querySelectorAll('.tab-content').forEach((tab) => {
                tab.classList.remove('active');
            });
            document.querySelectorAll('.tab-button').forEach((button) => {
                button.classList.remove('active');
            });
            document.getElementById(tabId).classList.add('active');
            document.querySelector(`.tab-button[onclick="showTab('${tabId}')"]`).classList.add('active');
        }
    </script>
</body>
</html>
