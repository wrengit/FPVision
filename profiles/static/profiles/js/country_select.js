window.onload = () => {
  let countrySelected = document.getElementById("id_default_country");
  if (!countrySelected.value) {
    countrySelected.style.color = "rgba(54, 54, 54, 0.3)";
  }
  countrySelected.onchange = () => {
    if (!countrySelected.value) {
      countrySelected.style.color = "rgba(54, 54, 54, 0.3)";
    } else {
      countrySelected.style.color = "#363636";
    }
  };
};
