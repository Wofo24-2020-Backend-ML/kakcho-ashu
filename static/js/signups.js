console.log(9+3);

document.querySelector("#rr_submit").addEventListener("click", async () => {
  const data = {
    email: document.querySelector("#rr_email").value,
    username: document.querySelector("#rr_name").value,
    password: document.querySelector("#rr_password").value,
  };
  const response = await axios.post(
    "https://kakcho-ashu.herokuapp.com/auth/register/",
    data
  );
  console.log(response);
});
