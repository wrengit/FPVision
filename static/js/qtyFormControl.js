function qtyFormControl() {
    let timer = null
    return {
        handleEnableDisable(targetId) {
            let input = document.getElementById(`qty-${targetId}`);
            let currentVal = parseInt(input.value);
            let maxVal = parseInt(input.getAttribute("max"));
            let minusDisabled = currentVal < 2;
            let plusDisabled = currentVal > maxVal - 1;
            let increment = document.getElementById(`increment-${targetId}`);
            let decrement = document.getElementById(`decrement-${targetId}`);
            if (minusDisabled) {
                decrement.setAttribute("disabled", "");
            } else if (plusDisabled) {
                increment.setAttribute("disabled", "");
            } else {
                increment.removeAttribute("disabled");
                decrement.removeAttribute("disabled");
            }
        },
        updateSubmitForm(targetId) {
            timer = setTimeout(() => {
                let form = document.getElementById(`basket-quantity-form-${targetId}`);
                let input = document.getElementById(`qty-${targetId}`);
                let currentVal = parseInt(input.value);
                let maxVal = parseInt(input.getAttribute("max"));
                if (currentVal > maxVal) {
                    input.value = maxVal;
                }
                if (window.location.pathname == "/basket/") {
                    form.submit();   
                }
                
            }, 800)
            this.handleEnableDisable(targetId)
        },
        incrementQty(targetId) {
            let input = document.getElementById(`qty-${targetId}`);
            let currentVal = parseInt(input.value);
            let maxVal = parseInt(input.getAttribute("max"));
            if (input.value < maxVal) {
                input.value = currentVal + 1;
            } else {
                input.value = maxVal;
            }
            this.handleEnableDisable(targetId);
            if (window.location.pathname == "/basket/") {
                if (timer) {
                    clearTimeout(timer)
                    timer = null
                }
                this.updateSubmitForm(targetId)
            }
        },
        decrementQty(targetId) {
            let input = document.getElementById(`qty-${targetId}`);
            let currentVal = parseInt(input.value);
            let maxVal = parseInt(input.getAttribute("max"));
            if (input.value > 0 && input.value > maxVal) {
                input.value = maxVal;
            } else if (input.value > 0) {
                input.value = currentVal - 1;
            }
            this.handleEnableDisable(targetId);
            if (window.location.pathname == "/basket/") {
                if (timer) {
                    clearTimeout(timer)
                    timer = null
                }
                this.updateSubmitForm(targetId)
            }

        },
        //https://stackoverflow.com/questions/19966417/prevent-typing-non-numeric-in-input-type-number
        blockAlpha(e) {
            if (
                (e.key.length === 1 &&
                    e.key !== "." &&
                    isNaN(e.key) &&
                    !e.ctrlKey) ||
                (e.key === "." &&
                    e.target.value.toString().indexOf(".") > -1)
            ) {
                e.preventDefault();
            }
        },
    };
}