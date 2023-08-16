import java.applet.Applet;
import java.awt.Label;
import java.awt.TextField;
import java.awt.event.TextEvent;
import java.awt.event.TextListener;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class LastNameFinderApplet extends Applet implements TextListener {
    private TextField firstNameField;
    private Label lastNameLabel;

    @Override
    public void init() {
        firstNameField = new TextField(20);
        firstNameField.addTextListener(this);

        lastNameLabel = new Label();

        add(new Label("Enter First Name:"));
        add(firstNameField);
        add(new Label("Last Name:"));
        add(lastNameLabel);
    }

    @Override
    public void textValueChanged(TextEvent e) {
        String firstName = firstNameField.getText().toLowerCase();
        String matchingLastName = "";

        try (BufferedReader reader = new BufferedReader(new FileReader("lastnames.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] nameParts = line.split(":");
                if (nameParts[0].toLowerCase().equals(firstName)) {
                    matchingLastName = nameParts[1];
                    break;
                }
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }

        lastNameLabel.setText(matchingLastName.isEmpty() ? "Not found" : matchingLastName);
    }
}
