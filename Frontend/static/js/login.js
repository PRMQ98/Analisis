document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
  
    const username = document.getElementById("user").value;
    const password = document.getElementById("password").value;
  
    // Realizar la solicitud POST a la API utilizando Axios
    axios.post("http://localhost:5000/api/login", { username, password })
      .then(response => {
        if (response.status === 200) {
          const usuario = response.data.Usuario;
          const Id = response.data.Id;
          const pasteles = response.data.Pasteles;
          const menus = response.data.Menus;
          const submenus = response.data.Submenus;
          const precio = response.data.Precio;
          localStorage.setItem("Menus", JSON.stringify(menus));
          localStorage.setItem("Submenus", JSON.stringify(submenus));
          localStorage.setItem('Precio', precio);
          localStorage.setItem("Pasteles", JSON.stringify(pasteles)); 
          localStorage.setItem("Usuario", usuario)
          localStorage.setItem("Id",Id);
          window.location.href = "/templates/inicio.html";
        } else {
          alert("Credenciales inválidas");
        }
      })
      .catch(error => {
        console.error("Error al realizar la solicitud:", error);
      });
  });
  
  function validatePassword(password) {
    var passwordError = document.getElementById("passwordError");
    
    var criteria = [];

    if (password.length === 0) {
        passwordError.textContent = "";
        return;
    }
    if (password.length < 8) {
        criteria.push("al menos 8 caracteres");
    }
    
    if (!/(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9])/.test(password)) {
        criteria.push("una letra mayúscula, un número y un carácter especial");
    }
    
    if (/[./]/.test(password)) {
        criteria.push("no puede contener los caracteres '.' '/'");
    } 
    
    if (criteria.length > 0) {
        passwordError.textContent = "La contraseña debe contener " + criteria.join(", ") + ".";
    } else {
        passwordError.textContent = "";
    }
}