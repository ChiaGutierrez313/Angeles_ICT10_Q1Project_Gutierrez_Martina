from pyscript import document
from pyscript.ffi import create_proxy

def generate_sku(event=None):
    category = document.querySelector("#category").value
    product = document.querySelector("#sku_product").value
    stock_text = document.querySelector("#stock_quantity").value

    if category == "" or product == "":
        document.querySelector("#sku_output").textContent = "Please select a category and product."
        return

    try:
        stock_quantity = int(stock_text)
    except ValueError:
        document.querySelector("#sku_output").textContent = "Please enter a valid stock quantity."
        return

    if stock_quantity < 1:
        document.querySelector("#sku_output").textContent = "Stock quantity must be at least 1."
        return

    product_code = product.replace(" ", "").upper()

    sku = category + "-" + product_code + "-" + str(stock_quantity)

    document.querySelector("#sku_output").textContent = f"Generated SKU: {sku}"


sku_button = document.querySelector("#sku_button")

if sku_button:
    sku_button.addEventListener("click", create_proxy(generate_sku))