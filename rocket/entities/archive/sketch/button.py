from .element import Element
import stringcase


class Button(Element):

    def parse_specific_info(self):
        self.data['label_element'] = None
        self.data['icon_element'] = None

        self.set_content()

    @classmethod
    def type(cls):
        return "Button"

    @classmethod
    def should_export_component(cls) -> bool:
        return True

    def component_name(self) -> str:
        return stringcase.capitalcase(self.name) + 'Button'

    def component_template_name(self) -> str:
        return 'react_native/components/button.tmpl'

    def set_content(self):
        self._set_content(self.elements)

    def has_icon(self) -> bool:
        return self.data['icon_element'] is not None

    def get_icon_name(self) -> str:
        if not self.has_icon():
            return "None"

        return self.data['icon_element'].name

    def get_import_statements(self):
        return """
import %sButton from "./components/%sButton";        
        """ % (self.name, self.name)

    def _set_content(self, elements):
        if elements is None:
            return
        for element in elements:
            if element.name.startswith('LABEL_') and element.type() == 'Label':
                self.data['label_element'] = element
            elif element.name.startswith('ICON_') and element.type() == 'Icon':
                self.data['icon_element'] = element
            else:
                self._set_content(element.elements)

    def get_label_text(self):
        if self.data['label_element'] is None:
            return "BUTTON"

        return self.data['label_element'].get_text()

    def get_additional_functions(self):
        return """
    @autobind
    handleOnPress%sButton() {
        const {SessionStore, ScreenStore, navigation} = this.props;
    }
        """ % self.name

    def get_import_lines(self):
        return """
import %sButton from "./components/%sButton";
        """ % (self.name, self.name)

    def generate_react_native_component(self):
        if self.elements is None or len(self.elements) == 0:
            return '<View style={styles.%s}/>' % self.name

        if self.has_icon():
            return """
    <%sButton
        onPress={this.handleOnPress%sButton}
        label="%s"
        iconName="%s"
        iconColor="%s"
    />
            """ % (self.name, self.name, self.get_label_text(), self.name, self.name)

        return """
    <%sButton
        onPress={this.handleOnPress%sButton}
        label="%s"
    />
            """ % (self.name, self.name, self.get_label_text())
