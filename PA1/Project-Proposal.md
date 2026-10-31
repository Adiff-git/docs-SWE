# **B \- Project Proposal**

**Performed by:** Lê Đức Thịnh, Phan Thị Thanh Huyền, Nguyễn Công Kiên

**Reviewed by:** Nguyễn Hoàng Gia

## **Introduction**

Our project is an e-commerce website for an electronics store.   
Customers can browse and search the full product catalog, compare specifications, add items to a cart, check out with delivery or in-store pickup, pay for their order, and track its progress. Store staff can manage products, stock levels, orders, promotions, and customer reviews through a dedicated admin side of the same site. An AI product advisor helps shoppers who are unsure what to buy.

The site offers an alternative to in-person shopping that saves customers a trip to the store and gives them the information they need to choose confidently. For the store, it keeps product, stock, and sales records in one system, reducing manual work and errors. 

## **Target User and Environment**

Our main users are customers who want to buy electronic devices and accessories but may not be technically savvy and do not want to spend much time researching. Simple navigation, clear specifications, product comparison, and AI guidance are designed for them. The second type of user is the store owner or administrator, who manages the catalog, stock, orders, promotions, and customer accounts.

The application is a web application used on desktop. It runs in modern browsers Chrome,  Firefox on Windows, Linux and requires an internet connection. 

## **Key Features**

Features are divided into functional groups, dictated as follows.

1. ### Authentication 

- Sign up**:** New customers create an account with their name, email, and password. The system checks that the email isn't already registered and that the password meets basic rules. An account lets customers save their details, place orders, and view their history.  
- Log in and log out**:** Registered users sign in with their credentials and end their session safely with log out. The system sends customers and admins to the correct interface based on their role, so each sees only what they are allowed to use.  
- Password recovery**:** Users who forget their password can request a reset link by email and set a new one. This keeps them from being locked out of their orders and saved information.


2. ### Profile Management

- Edit personal information**:** Customers can view and update their name, phone number, and other basic details. Keeping this information current means orders and communications reach the right person.  
- Address book**:** Customers can save several delivery addresses, edit or delete them, and mark one as the default. This speeds up checkout, since they pick a saved address rather than retyping it.  
- Change password**:** Logged-in users can change their password by entering the current one and a new one. This lets them keep their account secure without going through recovery.

3. ### Search and Browse

- ### Search**:** Customers type a product name, brand, or keyword and get a list of matching products. Searching is the fastest way to a specific item in a large catalog.

- ### Filter and sort**:** Customers narrow results by category, brand, price range, and key specifications such as RAM or storage, and sort them by price or popularity. Electronics buyers choose by specifications, so filters help them cut a long list down to suitable products.

- ### Product details**:** Each product page shows images, price, discount, description, full specifications, stock availability, and ratings. Customers get everything they need to decide on one page, and can add the product to the cart from there.

- Product comparisons: Customers can select two or three products from the same category and view their technical specifications side by side in one table. This lets shoppers weigh options directly and see exactly how products differ, rather than opening each page separately.  
- Restock alerts: On the page of an out-of-stock product, customers can ask to be notified when it is available again and receive an email once the admin restocks it. This saves them from checking the page repeatedly, and the store keeps a sale it would otherwise lose.

4. ### Shopping Cart 

- Add to cart**:** Customers add a product, including its chosen variant such as color or storage, from the product page or listing. The cart keeps items together until they are ready to buy, so they can keep browsing.  
- Edit cart**:** Customers can change quantities, remove items, and select which items to check out. The system blocks quantities above available stock. This gives customers control over their order before paying and prevents orders for unavailable items.   
- Cart summary**:** The cart shows each item's price, the subtotal, and the running total. The cart is saved to the customer's account, so it is still there the next time they log in. Seeing totals early avoids surprises at checkout.


5. ### Checkout \+ Payment 

- Delivery details: During checkout, customers choose where their order goes by selecting a saved address, entering a new one, or editing the recipient's name and phone number for that order. If the store offers pickup, they can choose that instead. This saves customers from retyping details and lets them send orders to someone else.  
- Order review and discounts: Before paying, customers see a summary of their order: the items and quantities, the delivery method and fee, any applied voucher, and the final total. They can enter a voucher code and see the discount applied immediately. Seeing the full cost upfront lets customers catch mistakes and avoid surprises at payment.  
- Payment: Customers pay with cash on delivery, bank transfer or QR code, or a card or e-wallet through a payment gateway. Once payment is confirmed, the order status updates automatically. Offering several methods suits different customers, and handing card details to the gateway keeps sensitive data out of our system.


6. ### Product Management 

- Sales overview: Allow the seller to see an overview of each item that they are selling, including current displayed information (name, image, pricing, etc.) and also business statistics (stock number, number of sales, total revenue, etc.). This feature allows sellers a comprehensive view of their operation.  
- Create/Edit item: Admins can create a new product listing or update an existing one, including its name, category, images, price, description, and technical specifications. This keeps the storefront accurate, and the specifications entered here feed the comparison and filters customers use.  
- Stock management**:** Admins can view and update the quantity available for each product, and the system lowers it automatically when an order is placed and restores it if the order is cancelled. Products that reach zero are shown as out of stock and can’t be added to the cart, and the admin can see which items are running low. This prevents the store from selling items it doesn’t have and shows the admin when to restock.  
- Delete/Deactivate item: Temporarily hide or permanently remove an item (e.g. seasonal products) without losing its sales history. This lets the seller keep track of many promotional events and be able to plan more efficiently.

7. Order Management   
- Orders history: Customers can see a list of their past orders, each with its date, items, and total, and open any order to view its full details, such as the delivery address, payment method, and a summary of what was bought. This gives customers a record of their purchases and a way to check a transaction later.  
- Order tracking: Customers can see the current stage of each order, for example confirmed, packed, shipped, or delivered. This keeps them informed about where their purchase is and reduces the need to contact the store.  
- Order processing (admin): Admins can view all incoming orders, filter them by status or date, and update each order's status as it moves through confirmation, packing, shipping, and delivery. The status shown to the customer updates automatically, so the store and customer always see the same information.

8. ### Review \+ Rating 

- Submit review and rating: After receiving an order, buyers can rate the product from 1 to 5 stars and add a written review of their experience. Only verified purchasers can do this, so shoppers can trust that the feedback comes from real customers.  
- Ratings summary: Each product page shows its average score and a breakdown by star level, and the average also appears in search results. This lets buyers compare products and judge quality at a glance.

9. ### Store Administration  

- Store settings and homepage content: Admins can update homepage banners, featured products, shipping fees, accepted payment methods, and branch details. This keeps the storefront current without a developer making each change.  
- Review moderation**:** Admins can view reviews, including those reported by customers, and hide or delete ones that contain spam, abuse, or irrelevant content. This keeps product pages trustworthy and useful for other shoppers.  
- Customer account management**:** Admins can search the customer list, view account details, and deactivate or reactivate accounts. This lets the store respond to fraud or repeated misuse without needing technical access to the database.  
- Promotions and vouchers: Admins can create sales events and voucher codes with a set period, discount type, and the products or categories included. This helps the store run campaigns such as holiday sales without changing each product by hand.

### 10\. Agent Chatbox and Automation

A chat assistant on the storefront that understands requests in everyday language and answers them or acts on them using the store’s catalog and the customer’s account. 	

- Guided product discovery: Customers describe what they need in everyday language, such as “a laptop for university and light video editing under 25 million VND”, and the assistant asks follow-up questions and shows matching products from the catalog. It can also recommend products, compare models, and suggest compatible accessories or alternatives, explaining the differences in plain language. This helps non-technical shoppers choose without reading specification tables or guessing which filters to use.  
- Automated shopping actions: Customers can ask the assistant to carry out steps for them, such as adding, removing, or replacing items in the cart, or preparing checkout with a saved address and delivery option. The assistant asks for missing details and shows the result after each action, and the customer still confirms the order and pays. This lets customers build an order by chatting while the final decision stays with them.  
- Order and stock assistance: Logged-in customers can ask about their orders, for example “Where is my latest order?”, and get the current status and tracking details in the chat. They can also ask to be notified by email when an out-of-stock item is available again. This answers common questions quickly and saves customers from checking pages repeatedly.

### 