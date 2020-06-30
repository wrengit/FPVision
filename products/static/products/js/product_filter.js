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
                if (priceList[i].parentNode.style.display == "block") {
                    maxPriceArr.push(priceList[i].textContent)
                }
            }
            maxPriceArr.sort((a, b) => b - a)
            this.maxPrice = maxPriceArr[0]
        },
        findMinPrice() {
            let minPriceArr = []
            for (let i = 0; i < priceList.length; i++) {
                if (priceList[i].parentNode.style.display == "block") {
                    minPriceArr.push(priceList[i].textContent)
                }
            }
            minPriceArr.sort((a, b) => a - b)
            this.minPrice = minPriceArr[0]
        },
        stockFilter() {
            switch (true) {
                case inStockCheck.checked && !outStockCheck.checked:
                    for (let i = 0; i < stockList.length; i++) {
                        stockList[i].parentNode.style.display =
                            stockList[i].textContent == 0 ?
                            "none" : "block"
                    }
                    this.findMaxPrice()
                    this.findMinPrice()
                    break;
                case !inStockCheck.checked && outStockCheck.checked:
                    for (let i = 0; i < stockList.length; i++) {
                        stockList[i].parentNode.style.display =
                            stockList[i].textContent > 0 ?
                            "none" : "block"
                    }
                    this.findMaxPrice()
                    this.findMinPrice()
                    break;
                default:
                    for (let i = 0; i < stockList.length; i++) {
                        stockList[i].parentNode.style.display = "block"
                    }
                    this.findMaxPrice()
                    this.findMinPrice()
                    break;
            }

        },
        priceFilter() {
            for (let i = 0; i < priceList.length; i++) {
                if (
                    (parseFloat(maxPriceInput.value) >=
                    parseFloat(priceList[i].textContent) ||
                    maxPriceInput.value == "") &&
                    (parseFloat(minPriceInput.value) <=
                    parseFloat(priceList[i].textContent) ||
                    minPriceInput.value == "")
                    ) {
                        priceList[i].parentNode.style.display = "block"
                    } else {
                        priceList[i].parentNode.style.display = "none"
                    }
                } 


        },
        resetFilters() {
            inStockCheck.checked = false
            outStockCheck.checked = false
            this.stockFilter()
        }

    }
}