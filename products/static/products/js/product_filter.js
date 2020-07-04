function productFilter() {
  let stockList = document.querySelectorAll("div.hideme-stock");
  let priceList = document.querySelectorAll("div.hideme-price");
  let inStockCheck = document.getElementById("in-stock-check");
  let outStockCheck = document.getElementById("out-stock-check");
  let minPriceInput = document.getElementById("min-price-filter");
  let maxPriceInput = document.getElementById("max-price-filter");
  let subCatCheckList = document.querySelectorAll("input.subcatcheck");
  let catCheckList = document.querySelectorAll("input.catcheck");
  let filterNav = document.querySelector("aside.sticky-filter");
  let overlay = document.querySelector("div.overlay");
  let i;

  return {
    maxPrice: "",
    minPrice: "",
    findMinMaxPrice() {
      let priceArr = [];
      for (i = 0; i < priceList.length; i++) {
        priceArr.push(priceList[i].textContent);
      }
      priceArr.sort((a, b) => b - a);
      this.maxPrice = priceArr[0];
      this.minPrice = priceArr.slice(-1)[0];
    },

    stockPriceFilter() {
      // Add checked subcategory names to an array
      let subCatChecked = [];
      for (i = 0; i < subCatCheckList.length; i++) {
        if (subCatCheckList[i].checked) {
          subCatChecked.push(subCatCheckList[i].name);
        }
      }
      // Add checked category names to an array
      let catChecked = [];
      for (i = 0; i < catCheckList.length; i++) {
        if (catCheckList[i].checked) {
          catChecked.push(catCheckList[i].name);
        }
      }
      for (i = 0; i < stockList.length; i++) {
        let productNode = stockList[i].parentNode;
        let subCategoryName = stockList[i].attributes.name.textContent;
        let categoryName = priceList[i].attributes.name.textContent;
        // Boolean to determine if products are in subCatCheck array
        let subCatTrue =
          subCatChecked.includes(subCategoryName) || subCatChecked.length == 0;
        // Boolean to determine if products are in catCheck array
        let catTrue =
          catChecked.includes(categoryName) || catChecked.length == 0;
        let minPriceLower =
          parseFloat(minPriceInput.value) <=
            parseFloat(priceList[i].textContent) || minPriceInput.value == "";
        let maxPriceHigher =
          parseFloat(maxPriceInput.value) >=
            parseFloat(priceList[i].textContent) || maxPriceInput.value == "";
        stockLevel = parseInt(stockList[i].textContent);

        allTrue = maxPriceHigher && minPriceLower && subCatTrue && catTrue;

        // Check each product against current filters
        switch (true) {
          case inStockCheck.checked && !outStockCheck.checked:
            productNode.style.display =
              allTrue && stockLevel > 0 ? "block" : "none";
            break;

          case !inStockCheck.checked && outStockCheck.checked:
            productNode.style.display =
              allTrue && stockLevel == 0 ? "block" : "none";
            break;

          default:
            productNode.style.display = allTrue ? "block" : "none";
            break;
        }
      }
    },

    // Close filter when user clicks away
    handleCloseFilter(e) {
      if (!e.target.closest("#filter-container")) {
        if (filterNav.style.transform == "translateX(-22rem)") {
          filterNav.style.transform = "translateX(2.5rem)";
          overlay.classList.toggle("fade");
        }
      }
    },

    // Toggle filter open/closed
    handleShowHideFilter() {
      filterNav.style.transform =
        filterNav.style.transform == "translateX(-22rem)"
          ? "translateX(2.5rem)"
          : "translateX(-22rem)";
      overlay.classList.toggle("fade");
    },

    // Uncheck 'stock' and 'sub categories' filters and find the
    // product list min and max price
    resetFilters() {
      this.findMinMaxPrice();
      inStockCheck.checked = false;
      outStockCheck.checked = false;
      for (i = 0; i < subCatCheckList.length; i++) {
        subCatCheckList[i].checked = false;
      }
      for (i = 0; i < catCheckList.length; i++) {
        catCheckList[i].checked = false;
      }
    },
  };
}
