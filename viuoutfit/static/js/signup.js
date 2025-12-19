document.getElementById("signupForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Stop form from submitting

    // Get input values
    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value.trim();
    let confirmPassword = document.getElementById("confirmPassword").value.trim();

    // Get error message elements
    let nameError = document.getElementById("nameError");
    let emailError = document.getElementById("emailError");
    let passwordError = document.getElementById("passwordError");
    let confirmPasswordError = document.getElementById("confirmPasswordError");

    // Clear old errors
    nameError.textContent = "";
    emailError.textContent = "";
    passwordError.textContent = "";
    confirmPasswordError.textContent = "";

    let valid = true;

    // Name validation
    if (name === "") {
        nameError.textContent = "Full name is required";
        valid = false;
    }

    // Email validation
    if (email === "") {
        emailError.textContent = "Email is required";
        valid = false;
    }

    // Password validation
    if (password === "") {
        passwordError.textContent = "Password is required";
        valid = false;
    } else if (password.length < 6) {
        passwordError.textContent = "Password must be at least 6 characters";
        valid = false;
    }

    // Confirm password validation
    if (confirmPassword === "") {
        confirmPasswordError.textContent = "Please confirm your password";
        valid = false;
    } else if (password !== confirmPassword) {
        confirmPasswordError.textContent = "Passwords do not match";
        valid = false;
    }

    // If everything is valid
    if (valid) {
        alert("Signup successful!");
        // You can redirect to login page here:
        // window.location.href = "login.html";
    }
});