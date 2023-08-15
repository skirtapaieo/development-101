def probability_of_disease(accuracy, prevalence)

    # Positive Predictive Value (PPV)
    ppv = (accuracy * prevalence) / (accuracy * prevalence + (1 - accuracy) * (1 - prevalence))

    # Negative Predictive Value (NPV)
    npv = (accuracy * (1 - prevalence)) / ((1 - accuracy) * prevalence + accuracy * (1 - prevalence))

    return [round(ppv, 4), round(npv, 4)]

accuracy = 0.95
prevalence = 0.03
print(probability_of_disease(accuracy, prevalence))


