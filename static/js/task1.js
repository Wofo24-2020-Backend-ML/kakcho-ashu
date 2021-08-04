console.log(7+3);

document.querySelector("#rr_submit").addEventListener("click", async () => {
  const data = {
    file: document.querySelector("#rr_file").value,
    column_name: document.querySelector("#rr_column_name").value,
  };
  const response = await axios.post(
    "https://kakcho-ashu.herokuapp.com/csvupload/task2",
    data
  );
  console.log(response);
  localStorage.setItem("access", response.data.tokens.access);
  localStorage.setItem("refresh", response.data.tokens.refresh);
});
