python3 -m venv venv
activate(){
    . venv/bin/activate
    echo "Installing requirements to cirtual environment"
    pip install -r requirements.txt
}
activate

