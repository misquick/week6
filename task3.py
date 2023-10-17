try:
    file_input = input("Enter file name: ")
    count = 0
    total_confidence = 0

    with open(file_input, 'r') as file:
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                try:
                    confidence = float(line.split(":")[1].strip())
                    total_confidence += confidence
                    count += 1
                except ValueError:
                    continue

    if count > 0:
        average_confidence = total_confidence / count
        print(f"Average spam confidence: {average_confidence:.14f}")
    else:
        print("X-DSPAM-Confidence lines were not found in the file.")

except FileNotFoundError:
    print("File cannot be opened")
