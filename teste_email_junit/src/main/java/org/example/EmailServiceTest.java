package org.example;

import org.junit.Test;

import static org.junit.Assert.assertThrows;

public class EmailServiceTest {
    @Test
    public void testEnviarEmailComEmailInvalido() {
        EmailService emailService = new EmailService();
        String emailInvalido = "emailsemarroba.com";
        assertThrows(IllegalArgumentException.class, () -> {
            emailService.enviarEmail(emailInvalido);
        });
    }
    @Test
    public void testEnviarEmailComEmailNulo() {
        EmailService emailService = new EmailService();
        assertThrows(IllegalArgumentException.class, () -> {
            emailService.enviarEmail(null);
        });
    }

    @Test
    public void testEnviarEmailComEmailVazio() {
        EmailService emailService = new EmailService();
        assertThrows(IllegalArgumentException.class, () -> {
            emailService.enviarEmail("");
        });
    }
    @Test
    public void testEnviarEmailComMultiplosArrobas() {
        EmailService emailService = new EmailService();
        String emailComMultiplosArrobas = "usuario@@dominio.com";
        assertThrows(IllegalArgumentException.class, () -> {
            emailService.enviarEmail(emailComMultiplosArrobas);
        });
    }
    @Test
    public void testEnviarEmailSemPonto() {
        EmailService emailService = new EmailService();
        String emailSemPonto = "usuario@dominio";
        assertThrows(IllegalArgumentException.class, () -> {
            emailService.enviarEmail(emailSemPonto);
        });
    }




}
