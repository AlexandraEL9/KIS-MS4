from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    def open(self):
        """
        Ensure that no unexpected arguments like `keyfile` are passed to `starttls()`.
        """
        if self.connection:
            return False
        try:
            self.connection = self.connection_class(
                self.host,
                self.port,
                **self.connection_params
            )
            if self.use_tls:
                self.connection.ehlo()
                self.connection.starttls()  # Ensures no extra arguments are passed
                self.connection.ehlo()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except Exception as e:
            if not self.fail_silently:
                raise
            return False
