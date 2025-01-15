function initializeCharts(data) {
    const colors = {
        excellent: 'rgba(40, 167, 69, 0.8)',
        good: 'rgba(23, 162, 184, 0.8)',
        average: 'rgba(255, 193, 7, 0.8)',
        poor: 'rgba(220, 53, 69, 0.8)'
    };

    const options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    callback: function(value) {
                        return value + '%';
                    }
                }
            }
        },
        plugins: {
            legend: {
                position: 'bottom'
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return context.dataset.label + ': ' + context.parsed.y + '%';
                    }
                }
            }
        }
    };

    // Initialize charts with data passed from Django view
    // This function would be called from the statistics template
}