"""
A simple prototype tool to convert high-level business requirements into low-level technical specifications.
The tool breaks down the input requirement into modules, schemas, and pseudocode using simple rule-based logic.
"""

import sys

def analyze_requirement(requirement_text):
    """
    Analyze the high-level requirement text and break it down into:
    - Modules: functional components
    - Schemas: data entities and their attributes
    - Pseudocode: basic logic for each module
    """
    # For prototype, use simple keyword-based splitting and templates
    
    # Example keywords to identify modules
    module_keywords = ['user', 'account', 'payment', 'order', 'inventory', 'notification', 'report']
    
    # Identify modules mentioned in the requirement
    modules = []
    for keyword in module_keywords:
        if keyword in requirement_text.lower():
            modules.append(keyword.capitalize() + "Module")
    if not modules:
        modules.append("GeneralModule")
    
    # Define simple schemas based on modules
    schemas = {}
    for module in modules:
        if module == "UserModule":
            schemas['User'] = ['id', 'name', 'email', 'password']
        elif module == "AccountModule":
            schemas['Account'] = ['account_id', 'user_id', 'balance', 'status']
        elif module == "PaymentModule":
            schemas['Payment'] = ['payment_id', 'account_id', 'amount', 'date', 'status']
        elif module == "OrderModule":
            schemas['Order'] = ['order_id', 'user_id', 'items', 'total_price', 'status']
        elif module == "InventoryModule":
            schemas['InventoryItem'] = ['item_id', 'name', 'quantity', 'price']
        elif module == "NotificationModule":
            schemas['Notification'] = ['notification_id', 'user_id', 'message', 'date', 'read_status']
        elif module == "ReportModule":
            schemas['Report'] = ['report_id', 'type', 'generated_date', 'content']
        else:
            schemas[module.replace("Module", "")] = ['id', 'attribute1', 'attribute2']
    
    # Generate pseudocode for each module
    pseudocode = {}
    for module in modules:
        if module == "UserModule":
            pseudocode[module] = [
                "function createUser(name, email, password):",
                "    validate input",
                "    save user to database",
                "    return user_id",
                "",
                "function authenticateUser(email, password):",
                "    check credentials",
                "    return authentication token"
            ]
        elif module == "PaymentModule":
            pseudocode[module] = [
                "function processPayment(account_id, amount):",
                "    validate account and balance",
                "    deduct amount",
                "    record transaction",
                "    return payment confirmation"
            ]
        else:
            pseudocode[module] = [
                f"// Pseudocode for {module}",
                "function exampleFunction():",
                "    // implement logic here"
            ]
    
    return {
        "modules": modules,
        "schemas": schemas,
        "pseudocode": pseudocode
    }

def format_output(spec):
    """
    Format the specification dictionary into a readable string output.
    """
    output = []
    output.append("Modules:")
    for module in spec['modules']:
        output.append(f"- {module}")
    output.append("\nSchemas:")
    for schema, fields in spec['schemas'].items():
        output.append(f"- {schema}: {', '.join(fields)}")
    output.append("\nPseudocode:")
    for module, code_lines in spec['pseudocode'].items():
        output.append(f"{module}:")
        for line in code_lines:
            output.append(f"  {line}")
        output.append("")
    return "\n".join(output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python requirement_to_spec.py \"<high-level requirement>\"")
        sys.exit(1)
    requirement_text = sys.argv[1]
    spec = analyze_requirement(requirement_text)
    output = format_output(spec)
    print(output)

if __name__ == "__main__":
    main()
