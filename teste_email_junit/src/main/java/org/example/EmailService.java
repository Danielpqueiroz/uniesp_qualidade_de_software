package org.example;

public class EmailService {
    public void enviarEmail(String email) {
        if (email == null || !email.contains("@")) {
            throw new IllegalArgumentException("Email inválido: ausência de '@'.");
        }
        if (email.indexOf('@') != email.lastIndexOf('@')) {
            throw new IllegalArgumentException("Email inválido: múltiplos sinais de '@'.");
        }

        int atIndex = email.indexOf("@");
        String domainPart = email.substring(atIndex + 1);
        if (!domainPart.contains(".")) {
            throw new IllegalArgumentException("Email deve conter um ponto no domínio.");
        }
    }
}
