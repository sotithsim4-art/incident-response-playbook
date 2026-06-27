import datetime

playbooks = {
    "1": {
        "name": "Phishing Attack",
        "phases": [
            {
                "phase": "IDENTIFICATION",
                "steps": [
                    "Confirm the report — who received it and when?",
                    "Preserve the original email (do not delete it)",
                    "Check email headers for spoofed sender domains",
                    "Identify all recipients of the same email",
                    "Determine if any links were clicked or attachments opened",
                ]
            },
            {
                "phase": "CONTAINMENT",
                "steps": [
                    "Block the malicious sender domain at the email gateway",
                    "Quarantine the email from all affected mailboxes",
                    "Isolate any endpoint that clicked a link or opened an attachment",
                    "Reset credentials for any affected accounts",
                    "Revoke active sessions for compromised accounts",
                ]
            },
            {
                "phase": "ERADICATION",
                "steps": [
                    "Scan affected systems for malware or persistence mechanisms",
                    "Remove any malicious files or software found",
                    "Patch any vulnerabilities exploited by the attack",
                    "Verify no backdoors or unauthorized accounts were created",
                ]
            },
            {
                "phase": "RECOVERY",
                "steps": [
                    "Restore affected systems from clean backups if needed",
                    "Re-enable accounts after credentials are reset",
                    "Monitor affected systems for 72 hours for re-infection",
                    "Confirm normal operations have resumed",
                ]
            },
            {
                "phase": "LESSONS LEARNED",
                "steps": [
                    "Document a full timeline of the incident",
                    "Identify how the phishing email bypassed filters",
                    "Update email filtering rules based on findings",
                    "Conduct security awareness training for affected staff",
                    "File an official incident report",
                ]
            },
        ]
    },
    "2": {
        "name": "Ransomware Attack",
        "phases": [
            {
                "phase": "IDENTIFICATION",
                "steps": [
                    "Confirm ransomware infection — look for encrypted files and ransom note",
                    "Identify which systems and data are affected",
                    "Determine the ransomware variant if possible",
                    "Identify patient zero — how did it get in?",
                    "Document the time of first detection",
                ]
            },
            {
                "phase": "CONTAINMENT",
                "steps": [
                    "Immediately disconnect affected systems from the network",
                    "Disable shared drives and network shares",
                    "Block outbound connections from affected systems",
                    "Notify management and legal immediately",
                    "Do NOT pay the ransom without legal and executive approval",
                ]
            },
            {
                "phase": "ERADICATION",
                "steps": [
                    "Identify and remove the ransomware payload",
                    "Check for persistence mechanisms (scheduled tasks, registry keys)",
                    "Scan all systems on the same network segment",
                    "Patch the vulnerability used to gain initial access",
                ]
            },
            {
                "phase": "RECOVERY",
                "steps": [
                    "Restore systems from last known clean backup",
                    "Verify backup integrity before restoring",
                    "Rebuild systems from scratch if backups are compromised",
                    "Restore data in priority order — critical systems first",
                    "Monitor restored systems closely for 7 days",
                ]
            },
            {
                "phase": "LESSONS LEARNED",
                "steps": [
                    "Document how the ransomware entered the environment",
                    "Review backup procedures and test restoration process",
                    "Implement network segmentation to limit lateral movement",
                    "Report to FBI and CISA if critical infrastructure is affected",
                    "Update incident response plan with findings",
                ]
            },
        ]
    },
    "3": {
        "name": "Unauthorized Access",
        "phases": [
            {
                "phase": "IDENTIFICATION",
                "steps": [
                    "Review access logs to confirm unauthorized login",
                    "Identify the account and system that was accessed",
                    "Determine what data or resources were accessed",
                    "Check for signs of privilege escalation",
                    "Document the timeline of activity",
                ]
            },
            {
                "phase": "CONTAINMENT",
                "steps": [
                    "Disable the compromised account immediately",
                    "Terminate all active sessions for the account",
                    "Block the source IP address at the firewall",
                    "Preserve all logs before they rotate or are overwritten",
                ]
            },
            {
                "phase": "ERADICATION",
                "steps": [
                    "Audit all accounts for unauthorized changes",
                    "Remove any backdoor accounts created by the attacker",
                    "Review and tighten access control policies",
                    "Enable MFA on all privileged accounts",
                ]
            },
            {
                "phase": "RECOVERY",
                "steps": [
                    "Reset credentials for all potentially affected accounts",
                    "Restore any modified or deleted data from backups",
                    "Re-enable accounts only after credentials are secured",
                    "Monitor the environment for 72 hours",
                ]
            },
            {
                "phase": "LESSONS LEARNED",
                "steps": [
                    "Identify how the attacker obtained valid credentials",
                    "Review password policies and enforce complexity requirements",
                    "Evaluate whether additional monitoring is needed",
                    "Notify affected users and stakeholders per policy",
                    "File an official incident report",
                ]
            },
        ]
    },
}

def run_playbook():
    print("=" * 55)
    print("  INCIDENT RESPONSE PLAYBOOK")
    print("  Interactive step-by-step response guide")
    print("=" * 55)
    print("\nSelect incident type:")
    print("  1. Phishing Attack")
    print("  2. Ransomware Attack")
    print("  3. Unauthorized Access")

    while True:
        choice = input("\n  Enter 1, 2, or 3: ").strip()
        if choice in playbooks:
            break
        print("  Please enter 1, 2, or 3.")

    playbook = playbooks[choice]
    incident_name = playbook["name"]
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    completed_steps = []
    skipped_steps = []

    print(f"\n{'=' * 55}")
    print(f"  INCIDENT: {incident_name}")
    print(f"  Started:  {now}")
    print(f"  Mark each step C (Complete) or S (Skip)")
    print(f"{'=' * 55}")

    for section in playbook["phases"]:
        print(f"\n--- {section['phase']} ---")
        for step in section["steps"]:
            while True:
                action = input(f"  {step}\n  [C/S] > ").strip().upper()
                if action in ["C", "S"]:
                    break
                print("  Enter C to mark complete or S to skip.")
            if action == "C":
                completed_steps.append((section["phase"], step))
            else:
                skipped_steps.append((section["phase"], step))

    print_report(incident_name, now, completed_steps, skipped_steps)

def print_report(incident_name, started, completed, skipped):
    total = len(completed) + len(skipped)
    pct = round((len(completed) / total) * 100) if total > 0 else 0
    closed = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n{'=' * 55}")
    print(f"  INCIDENT RESPONSE SUMMARY")
    print(f"  Incident:  {incident_name}")
    print(f"  Opened:    {started}")
    print(f"  Closed:    {closed}")
    print(f"  Completed: {len(completed)}/{total} steps ({pct}%)")
    print(f"{'=' * 55}")

    if skipped:
        print(f"\n  SKIPPED STEPS — REQUIRE FOLLOW-UP:")
        for phase, step in skipped:
            print(f"    [{phase}] ✗ {step}")

    print(f"\n{'=' * 55}")
    if pct == 100:
        print("  STATUS: Incident fully resolved.")
    elif pct >= 70:
        print("  STATUS: Mostly resolved. Complete skipped steps.")
    else:
        print("  STATUS: Significant steps outstanding. Escalate.")
    print(f"{'=' * 55}")

    save = input("\nSave report to file? (Y/N): ").strip().upper()
    if save == "Y":
        filename = f"ir_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write(f"INCIDENT RESPONSE REPORT\n")
            f.write(f"Incident: {incident_name}\n")
            f.write(f"Opened: {started}\n")
            f.write(f"Closed: {closed}\n")
            f.write(f"Completed: {len(completed)}/{len(completed)+len(skipped)} steps ({pct}%)\n\n")
            f.write("COMPLETED STEPS:\n")
            for phase, step in completed:
                f.write(f"  [{phase}] ✓ {step}\n")
            if skipped:
                f.write("\nSKIPPED STEPS:\n")
                for phase, step in skipped:
                    f.write(f"  [{phase}] ✗ {step}\n")
        print(f"Report saved to {filename}")

run_playbook()
