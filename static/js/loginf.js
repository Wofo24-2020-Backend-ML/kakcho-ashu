console.log(97+3);

document.querySelector("#rr_submit").addEventListener("click", async () => {
  const data = {
    email: document.querySelector("#rr_email").value,
    password: document.querySelector("#rr_password").value,
  };
  const response = await axios.post(
    "https://kakcho-ashu.herokuapp.com/auth/login/",
    data
  );
  console.log(response);
  localStorage.setItem("access", response.data.tokens.access);
  localStorage.setItem("refresh", response.data.tokens.refresh);
});
