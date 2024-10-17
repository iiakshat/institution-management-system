// Function to dynamically load fee details
document.querySelectorAll('.pay-now-btn').forEach(button => {
    button.addEventListener('click', function() {
        const feeType = this.getAttribute('data-fee');
        const feeDetailsContainer = document.getElementById('fee-details');
        feeDetailsContainer.innerHTML = `
            <div class="fee-summary scrollable">
                <h2>Fee for Year - 4</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Sr. No</th>
                            <th>Fee Head</th>
                            <th>Fees To be Paid (₹)</th>
                            <th>Paid Amount (₹)</th>
                            <th>Outstanding Amount (₹)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>Tuition Fee</td>
                            <td>1,00,000</td>
                            <td>50,000</td>
                            <td>50,000</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>University Examination Fees</td>
                            <td>14,000</td>
                            <td>7,000</td>
                            <td>7,000</td>
                        </tr>
                    </tbody>
                </table>
                <button id="transaction-history-btn" class="transaction-btn">Transaction History</button>
                <button class="pay-now-btn">Pay Now</button> <!-- Added another 'Pay Now' button -->
            </div>
        `;
        feeDetailsContainer.style.display = 'block';

        // Transaction History Click Event
        document.getElementById('transaction-history-btn').addEventListener('click', function() {
            const transactionHistoryContainer = document.getElementById('transaction-history');
            transactionHistoryContainer.innerHTML = `
                <h2>Transaction History</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Payment Date</th>
                            <th>Amount Paid (₹)</th>
                            <th>Download Receipt</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>22-06-2024</td>
                            <td>50,000</td>
                            <td><button class="download-btn">Download</button></td>
                        </tr>
                    </tbody>
                </table>
            `;
            transactionHistoryContainer.style.display = 'block';
        });
    });
});
