# **Product Requirements: Real-time Order Tracking**

Author: Abhijit Das

## **Problem**

Currently, users of our online grocery delivery app lack detailed visibility into the status and location of their orders once they are dispatched. They receive a notification when the order is out for delivery, but there's no way to see the driver's real-time location or an estimated time of arrival (ETA) that dynamically updates. This lack of transparency leads to user anxiety, increased customer support inquiries about order status, and difficulty in planning their day around the delivery. Users often have to wait without knowing when to expect their groceries, impacting their overall experience.

## **Desired Outcomes**

**Expected Business Behaviour:**

  * Reduced volume of customer support inquiries related to order status.
  * Increased customer satisfaction and loyalty due to enhanced transparency.
  * Potential for improved delivery efficiency through better customer availability.

**Expected Product Behaviour:**

  * Users should be able to view the real-time location of their delivery driver on a map within the app.
  * The app should display a dynamic estimated time of arrival (ETA) that updates based on the driver's current location and traffic conditions.
  * Users should receive in-app notifications regarding significant updates to their delivery status (e.g., "Driver is 5 minutes away").

## **Measuring Success**

We will measure the success of the real-time order tracking feature by monitoring the following metrics:

| **Goal** | **Metric** |
| :-------------------------------------------- | :------------------------------------------------------------------------- |
| Decrease in "Where is my order?" inquiries | Percentage reduction in customer support tickets/calls related to order status. |
| Increase user engagement                      | Number of times users access the order tracking screen per order.          |
| Improve customer satisfaction                 | Increase in average customer satisfaction scores related to delivery experience (measured through post-delivery surveys). |
| Enhance app ratings                           | Increase in average app store ratings.                                     |

# **Designs**

[Link to Figma design mockups for the order tracking screen](https://www.google.com/search?q=insert_figma_link_here)

[Link to user flow diagram for order tracking](https://www.google.com/search?q=insert_user_flow_link_here)

## **Requirements**

| **Priority** | **Requirements** |
| :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High         | Users must be able to view a map displaying the real-time location of their assigned delivery driver once the order is out for delivery.                                      |
| High         | The app must display a dynamically updating Estimated Time of Arrival (ETA) for the delivery.                                                                                |
| High         | Users should receive in-app notifications for key delivery status updates, such as "Driver is on the way" and "Driver is arriving soon."                                     |
| High         | The driver's name and vehicle details (e.g., bike/car model and license plate number) should be visible to the user on the tracking screen for security and identification. |
| Medium       | Users should be able to contact the driver via a masked phone number through the app (while respecting privacy).                                                              |
| Medium       | The tracking map should provide visual cues for potential delays (e.g., traffic congestion).                                                                                 |
| Low          | Users should be able to share their live tracking link with others.                                                                                                           |
| Low          | The app should store a history of tracked deliveries for the user's reference.                                                                                                |

### \*\* Extra added info \*\*

  * **Technical Considerations:** Integration with GPS services, data privacy and security for location data, backend infrastructure for real-time updates.
  * **Future Enhancements:** Potential integration with estimated delivery window provided at the time of order placement, incorporating driver ratings after delivery.
  * **Out of Scope:** Offline tracking capabilities, integration with third-party map applications outside the app.