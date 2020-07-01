function productFilter() {
  let stockList = document.querySelectorAll("div.hideme-stock");
  let priceList = document.querySelectorAll("div.hideme-price");
  let inStockCheck = document.getElementById("in-stock-check");
  let outStockCheck = document.getElementById("out-stock-check");
  let minPriceInput = document.getElementById("min-price-filter");
  let maxPriceInput = document.getElementById("max-price-filter");
  let i;

  return {
    maxPrice: "",
    minPrice: "",
    findMinMaxPrice() {
      let priceArr = [];
      for (let i = 0; i < priceList.length; i++) {
        priceArr.push(priceList[i].textContent);
      }
      priceArr.sort((a, b) => b - a);
      this.maxPrice = priceArr[0];
      this.minPrice = priceArr.slice(-1)[0];
    },

    stockPriceFilter() {
      for (i = 0; i < stockList.length; i++) {
        let productNode = stockList[i].parentNode;
        let minPriceLower =
          parseFloat(minPriceInput.value) <=
            parseFloat(priceList[i].textContent) || minPriceInput.value == "";
        let maxPriceHigher =
          parseFloat(maxPriceInput.value) >=
            parseFloat(priceList[i].textContent) || maxPriceInput.value == "";
        stockLevel = stockList[i].textContent;

        // Check each product against current filters
        switch (true) {
          case inStockCheck.checked && !outStockCheck.checked:
            productNode.style.display =
              maxPriceHigher && minPriceLower && stockLevel > 0
                ? "block"
                : "none";
            break;

          case !inStockCheck.checked && outStockCheck.checked:
            productNode.style.display =
              maxPriceHigher && minPriceLower && stockLevel == 0
                ? "block"
                : "none";
          default:
            productNode.style.display =
              maxPriceHigher && minPriceLower ? "block" : "none";
            break;
        }
      }
    },

    // Uncheck 'stock' filters and find the whole product list
    // min and max price
    resetFilters() {
      this.findMinMaxPrice();
      inStockCheck.checked = false;
      outStockCheck.checked = false;
    },
  };
}
