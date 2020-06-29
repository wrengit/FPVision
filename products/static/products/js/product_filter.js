function productFilter() {
    let productList = document.querySelectorAll("div.hideme")
    let inStockCheck = document.getElementById("in-stock-check")
    let outStockCheck = document.getElementById("out-stock-check")


    return {
        stockFilter() {
            switch (true) {
                case inStockCheck.checked && !outStockCheck.checked:
                    for (let i = 0; i < productList.length; i++) {
                        if (productList[i].textContent == 0) {
                            productList[i].parentNode.style.display = "none"
                        }
                    }
                    break;
                case !inStockCheck.checked && outStockCheck.checked:
                    for (let i = 0; i < productList.length; i++) {
                        if (productList[i].textContent > 0) {
                            productList[i].parentNode.style.display = "none"
                        }
                    }
                    break;
                case !inStockCheck.checked && !outStockCheck.checked:
                    for (let i = 0; i < productList.length; i++) {
                        productList[i].parentNode.style.display = "block"
                    }
                    break;
                default:
                    for (let i = 0; i < productList.length; i++) {
                        productList[i].parentNode.style.display = "block"
                    }
            }
        }
    }
}