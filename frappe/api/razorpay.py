import frappe
import razorpay

@frappe.whitelist(allow_guest=True)
def create_order(amount):
    try:
        client = razorpay.Client(auth=("rzp_test_YrOxwBGGd3KQ3k", "F0KtppOchf61FwydnbFqTkdK"))

        order_data = {
            "amount": int(amount) * 100, 
            "currency": "INR",
            "payment_capture": 1 
        }

        order = client.order.create(order_data)

        return {"order_id": order["id"], "amount": order["amount"]}
    
    except Exception as e:
        frappe.log_error(f"Razorpay Error: {str(e)}", "Razorpay Payment")
        return {"error": str(e)}