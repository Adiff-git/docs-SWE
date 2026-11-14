# **Electronics Store E-commerce Website**

# **FG-04 \-- 023 \-- Manage Shopping Cart**

# 

# **Version 1.1**

# **Revision History**

| Date | Version | Description | Author |
| ----- | ----- | ----- | ----- |
| 14/Nov/26 | 1.0 | PA3 use-case specification transferred into team RUP template | Nguyễn Công Kiên |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

# **Table of Contents**

1\.	Use-Case Name	[4](#heading=h.oq89tnc9obnb)

1.1	Brief Description	[4](#heading=h.sf9je7joujv4)

2\.	Flow of Events	[4](#heading=h.te8t3th7oiwu)

2.1	Basic Flow	[4](#heading=h.uzq3vos3xg8p)  
2.2	Alternative Flows	[4](#heading=h.pjli10aqlkwc)  
2.2.1	Input validation and business-rule alternatives	[4](#heading=h.90nf2tgl97zx)  
2.2.2	Additional outcomes and service failures	[5](#heading=h.2jctwstndjhj)

3\.	Special Requirements	[5](#heading=h.jpoufo3fl2pf)

3.1	Use-case quality and integrity constraints	[5](#heading=h.l9khg2txct82)

4\.	Preconditions	[5](#heading=h.r0ozrurfkutp)

4.1	Conditions that must hold	[5](#heading=h.ifm3lbi0jlcx)

5\.	Postconditions	[5](#heading=h.67wlx6nqgmfj)

5.1	Success and failure states	[5](#heading=h.6ryofd6ik7w)

6\.	Extension Points	[5](#extension-points)

6.1	Related use cases and scope	[5](#heading=h.lxk9nkuz34js)

# **FG-04 \-- 023 \-- Manage Shopping Cart** 

1. # **Use-Case Name** 

   1. ## **Brief Description**

   A logged-in customer collects products in a cart before buying. The customer adds products with a chosen variant, changes quantities, removes items, and selects which items to check out. The system saves the cart to the customer's account, blocks quantities above available stock, and shows each item's price, the subtotal, and the running total. 

   Primary actor: Customer.

2. # **Flow of Events**

   1. ## **Basic Flow** 

1. The customer selects the cart icon in the header.  
2. The system loads the customer's saved cart and shows, for each item: image, product name, chosen variant (such as color or storage), unit price, quantity, line total, stock status, and a checkbox to select it for checkout.  
3. The system shows the subtotal and running total of the selected items. Delivery fees and vouchers are applied later, at checkout.  
4. The customer adjusts the cart as needed: changes an item's quantity (2.2.2), removes an item (2.2.3), or selects and deselects items for checkout (2.2.4).  
5. After each change, the system validates it against available stock, saves the cart to the customer's account, and refreshes the line totals, subtotal, and header cart count.  
6. The customer selects Checkout.  
7. The system confirms that at least one item is selected (2.2.8) and that every selected item is still available in the requested quantity (2.2.6).  
8. The system passes the selected items to the Checkout use case. The use case ends.  
   

   2. ## **Alternative Flows**

      1. ### *Add Product to Cart*

Starts instead of Basic Flow step 1, when the customer is on a product details page or a product listing.

1. The customer chooses a variant if the product has one, then selects Add to cart.  
2. The system checks that a variant is chosen, that the product is active, and that the variant is in stock. If no variant is chosen, the system asks the customer to pick one and adds nothing.  
3. If the same product and variant is already in the cart, the system increases its quantity by the chosen amount (1 by default). Otherwise it adds a new line, selected for checkout by default. If the new quantity would exceed stock, 2.2.5 applies.  
4. The system saves the cart, updates the header cart count, and shows a confirmation message.  
5. The customer keeps browsing, or opens the cart (Basic Flow step 1).  
   .

   2. ### *Change Item Quantity*

Start at Basic Flow step 4\.

1. The customer types a new quantity or uses the plus and minus controls on an item.  
2. The system checks that the quantity is a whole number of at least 1 and not above available stock. If the input is blank, zero, or not a number, the system restores the previous quantity and shows a message. If it is above stock, 2.2.5 applies.  
3. The system saves the quantity and updates the line total, subtotal, and header count.  
4. Resume at Basic Flow step 4\.

   3. ### *Change Item Quantity*

Start at Basic Flow step 4\.

1. The customer selects Remove on an item.  
2. The system deletes the item, saves the cart, and updates the subtotal and header count.  
3. If it was the last item, 2.2.7 applies. Otherwise resume at Basic Flow step 4\.

   4. ### *Select Items for Checkout*

Start at Basic Flow step 4\.

1. The customer ticks or unticks an item's checkbox, or uses select all.  
2. The system saves the selection and recalculates the subtotal from the selected items only. An item that is out of stock cannot be selected.  
3. Resume at Basic Flow step 4\.

   5. ### *Requested Quantity Exceeds Stock*

Starts at step 3 of 2.2.1 or step 2 of 2.2.2.

1. The system rejects the change and keeps the previous quantity.  
2. The system shows the available stock, for example "Only 3 left in stock".  
3. The customer chooses a smaller quantity. Resume at Basic Flow step 4\.

   6. ### *Item No Longer Available*

Starts at Basic Flow step 2 or 7, when a product in the cart was deactivated, sold out, or now has less stock than the cart quantity.

1. The system marks the item as unavailable (or shows how many are left) and clears its selection.  
2. The system leaves the item out of the subtotal and does not continue to checkout.  
3. The customer removes the item or lowers its quantity. Resume at Basic Flow step 4\.

   7. ### *Cart Is Empty*

Starts at Basic Flow step 2, or after the last item is removed.

1. The system shows an empty-cart message with a link back to the homepage, and disables Checkout.  
2. The use case ends.

   8. ### *No Items Selected*

Starts at Basic Flow step 7\.

1. The system does not continue and asks the customer to select at least one item.  
2. Resume at Basic Flow step 4\.

   

3. # **Special Requirements**

   

- ## Stock check on the server: every add and every quantity change is checked against current stock on the server, not only in the browser.

- ## Persistence: the cart belongs to the customer's account and is still there after logout and on another device or browser.

- ## Current prices: the cart shows the current catalog price. If a price changed since the item was added, the system shows the new price with a notice.

- ## Response time: cart changes should refresh within 2 seconds under normal load.

4. # **Preconditions**

   

- ## The customer is logged in with a customer account.

- ## For 2.2.1 only: the product is active and the chosen variant is in stock.

5. # **Postconditions**

- The cart saved to the customer's account matches the last confirmed items, quantities, and selection, and the header cart count matches it  
- If the customer continued, the selected items and quantities are handed to Checkout. The cart is not emptied by this use case.  
-  If a change was rejected or a system error occurred, the cart stays as last saved.


6. # **Extension Points** {#extension-points}

   

Proceed to Checkout: between Basic Flow steps 7 and 8, the Checkout use case continues from the selected items.

*Performed by: Nguyễn Công Kiên \| Reviewed by: Gia*