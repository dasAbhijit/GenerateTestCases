# **Product Requirements: Order Creation**

Author: Abhijit Das (adapted from Order Tracking BRD template)

## **Problem**

Currently, users of our online grocery delivery app may find the process of selecting groceries, adding them to a cart, and completing a purchase to be cumbersome, potentially time-consuming, or lacking in clarity. Challenges such as insufficient product information, difficulties in managing the shopping cart efficiently, or a non-intuitive checkout process can lead to user frustration and a high rate of cart abandonment. Users require a seamless, efficient, and user-friendly experience to browse products, make selections, and confidently complete their grocery purchases online.

## **Desired Outcomes**

**Expected Business Behaviour:**

* Increased conversion rates from Browse to completed orders.
* Reduced cart abandonment rates.
* Potential increase in Average Order Value (AOV) through intuitive upselling/cross-selling and ease of adding items.
* Improved user satisfaction and retention due to a smooth ordering experience.
* Efficient inventory display to minimize orders for out-of-stock items.

**Expected Product Behaviour:**

* Users can effortlessly search for grocery items using keywords and browse through well-defined categories.
* The app will display comprehensive product information, including price, detailed descriptions, high-quality images, nutritional information (where applicable), and current stock availability.
* Users can easily add items to their cart, remove items, and modify quantities with real-time updates to the cart summary.
* Users have the ability to save preferred items to a wishlist or create custom shopping lists for future convenience.
* Users experience a streamlined and secure multi-step checkout process, including clear selection for delivery address, available delivery slots, various payment options, and a final order review.
* Upon successful order placement, users will receive an immediate order confirmation (both in-app and via email/SMS) detailing the order summary, total cost, and the selected delivery window.

## **Measuring Success**

We will measure the success of the order creation feature enhancements by monitoring the following metrics:

| **Goal** | **Metric** |
| :--------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| Improve order completion rate                  | Percentage increase in the number of users successfully completing the checkout process (Orders/Sessions with cart activity). |
| Decrease cart abandonment rate                 | Percentage reduction in users abandoning their carts before completing a purchase.                          |
| Increase Average Order Value (AOV)             | Percentage increase in the average monetary value of successfully placed orders.                          |
| Enhance user satisfaction with ordering        | Improvement in customer satisfaction scores related to the ease of use and efficiency of the ordering process (measured via in-app surveys). |
| Reduce time to create an order                 | Percentage decrease in the average time taken by a user from first product addition to order confirmation. |
| Improve product discoverability                | Increase in product page views per session; successful search result rate.                                |

# **Designs**

[Link to Figma design mockups for product listing, product details, cart, and checkout screens](https://www.google.com/search?q=insert_figma_link_order_creation_here)

[Link to user flow diagram for the order creation process](https://www.google.com/search?q=insert_user_flow_order_creation_here)

## **Requirements**

| **Priority** | **Requirements** |
| :----------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High         | Users must be able to search for products using keywords (e.g., product name, brand, type) and browse products through a logical category and sub-category structure.        |
| High         | Product listing pages (e.g., search results, category pages) must display essential information: clear product name, primary image, current price, unit of measure (e.g., per kg, per item), and an "Add to Cart" button. |
| High         | Product detail pages must provide comprehensive information: multiple high-resolution images, detailed description, ingredients, nutritional information (if applicable), price, unit, stock availability status (e.g., "In Stock", "Low Stock", "Out of Stock"), and "Add to Cart" functionality. |
| High         | Users must be able to easily add items to their shopping cart, view the contents of their cart at any time, modify item quantities (increase/decrease/remove), and see real-time updates of the subtotal. |
| High         | The shopping cart screen must clearly display a detailed breakdown: list of items (name, quantity, price per item, total per item), subtotal for all items, estimated taxes, applicable delivery fees, and any applied discounts, leading to a clear grand total. |
| High         | The checkout process must be intuitive and guide the user through necessary steps: selection/confirmation of a delivery address (with an option to add a new address), choice of available delivery slots/times, selection from multiple payment methods (e.g., credit/debit card, digital wallets, COD if applicable), and a final order review page before payment. |
| High         | Upon successful payment and order placement, users must receive an immediate order confirmation both within the app (e.g., a success screen with order ID) and via a persistent notification method (e.g., email and/or SMS) containing the order summary, order ID, total amount paid, and the confirmed delivery address and time slot. |
| High         | System must accurately reflect product availability in real-time to prevent users from ordering out-of-stock items. If an item goes out of stock while in the user's cart, the user should be clearly notified. |
| Medium       | Users should be able to save items to a "Wishlist" or "Favorites" list for easy access and future purchase.                                                                  |
| Medium       | The system should provide relevant product suggestions, such as "Frequently Bought Together" or "Customers Also Bought," on product detail pages or in the cart.                 |
| Medium       | Users should have the ability to apply valid promotional codes or discount coupons at the cart or during checkout, with the discount clearly reflected in the total.             |
| Medium       | Users should be able to view their past order history, including item details and order status, and have an option to easily reorder an entire past order or specific items from it. |
| Medium       | Support for handling different product variants (e.g., size, weight, flavor) within a single product listing where applicable.                                                 |
| Low          | Users should be able to set up recurring orders (subscriptions) for frequently purchased items on a customizable schedule (e.g., weekly, monthly).                           |
| Low          | Users should have the option to add specific notes or instructions for their order (e.g., "Please select ripe bananas") or for the delivery (e.g., "Call upon arrival").       |

### **Extra added info**

* **Technical Considerations:**
    * Robust integration with a scalable Product Information Management (PIM) system and real-time Inventory Management System.
    * Secure payment gateway integration, ensuring PCI DSS compliance for handling sensitive cardholder data.
    * Scalable backend infrastructure (databases, APIs) to handle user accounts, product catalogs, order processing, and peak load times.
    * Integration with an address validation service to ensure accuracy of delivery addresses.
    * Efficient search functionality with typo tolerance and relevance ranking.
    * Session management to maintain cart persistence across user sessions (e.g., if the app is closed and reopened).
* **Future Enhancements:**
    * Advanced personalized product recommendations based on user's purchase history, Browse behavior, and collaborative filtering.
    * Integration with a customer loyalty program for earning and redeeming points.
    * "Quick Add" functionality from personalized shopping lists or based on predictive algorithms.
    * Voice-enabled search for finding products within the app.
    * Barcode scanning feature to quickly find and add products to the cart.
* **Out of Scope:**
    * Direct price comparison with competitor grocery stores.
    * In-app recipe builders that automatically add ingredients to the cart.
    * Social sharing of carts or wishlists.
    * Group or shared cart functionality for multiple users to contribute to a single order.
    * Bidding or auction features for products.