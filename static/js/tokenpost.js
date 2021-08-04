console.log(2+6)
document.querySelector("#rr_submit").addEventListener("click", async () => {
  const data = {
    auth_token: localStorage.getItem("ID Token"),

  };
  const response = await axios.post(
    "https://kakcho-ashu.herokuapp.com/google_auth/google/",
    data
  );
  auth_token =localStorage.getItem("ID Token")
  console.log(response.data.tokens);
  localStorage.setItem("access", response.data.tokens.access);
  localStorage.setItem("refresh", response.data.tokens.refresh);
});

