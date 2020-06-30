function productFilter() {
    let stockList = document.querySelectorAll("div.hideme-stock")
    let priceList = document.querySelectorAll("div.hideme-price")
    let inStockCheck = document.getElementById("in-stock-check")
    let outStockCheck = document.getElementById("out-stock-check")
    let minPriceInput = document.getElementById("min-price-filter")
    let maxPriceInput = document.getElementById("max-price-filter")


    return {
        maxPrice: "",
        minPrice: "",
        findMaxPrice() {
            let maxPriceArr = []
            for (let i = 0; i < priceList.length; i++) {
                maxPriceArr.push(priceList[i].textContent)
            }
            maxPriceArr.sort((a, b) => b - a)
            this.maxPrice = maxPriceArr[0]
        },

        findMinPrice() {
            let minPriceArr = []
            for (let i = 0; i < priceList.length; i++) {
                minPriceArr.push(priceList[i].textContent)
            }
            minPriceArr.sort((a, b) => a - b)
            this.minPrice = minPriceArr[0]
        },

        stockPriceFilter() {
            console.log("filter")
            switch (true) {
                case inStockCheck.checked && !outStockCheck.checked:
                    for (let i = 0; i < stockList.length; i++) {
                        stockList[i].parentNode.style.display =
                            (parseFloat(maxPriceInput.value) >=
                                parseFloat(priceList[i].textContent) ||
                                maxPriceInput.value == "") &&
                            (parseFloat(minPriceInput.value) <=
                                parseFloat(priceList[i].textContent) ||
                                minPriceInput.value == "") &&
                            stockList[i].textContent > 0 ?
                            "block" : "none"
                    }
                    break;

                case !inStockCheck.checked && outStockCheck.checked:
                    for (let i = 0; i < stockList.length; i++) {
                        stockList[i].parentNode.style.display =
                            (parseFloat(maxPriceInput.value) >=
                                parseFloat(priceList[i].textContent) ||
                                maxPriceInput.value == "") &&
                            (parseFloat(minPriceInput.value) <=
                                parseFloat(priceList[i].textContent) ||
                                minPriceInput.value == "") &&
                            stockList[i].textContent == 0 ?
                            "block" : "none"
                    }
                    break;
                default:
                    for (let i = 0; i < stockList.length; i++) {
                        stockList[i].parentNode.style.display =
                            (parseFloat(maxPriceInput.value) >=
                                parseFloat(priceList[i].textContent) ||
                                maxPriceInput.value == "") &&
                            (parseFloat(minPriceInput.value) <=
                                parseFloat(priceList[i].textContent) ||
                                minPriceInput.value == "") ?
                            "block" : "none"
                    }
                    break;
            }
        },
        resetFilters() {
            this.findMaxPrice()
            this.findMinPrice()
            inStockCheck.checked = false
            outStockCheck.checked = false
        }
    }
}