class Reporter:
    def generate_report(self, updates):
        report = "GitHub Repository Updates:\n"
        for repo, events in updates.items():
            report += f"\nRepository: {repo}\n"
            for event in events:
                report += f"- {event['type']} by {event['actor']['login']} at {event['created_at']}\n"
        return report
