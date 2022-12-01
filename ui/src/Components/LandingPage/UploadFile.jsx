import React from "react";
import axios from "axios";

class UploadFile extends React.Component {
    state = {
        files: null,
    };

    handleFile(e) {
        // Getting the files from the input
        let files = e.target.files;
        this.setState({ files });
    }

    handleUpload(e) {
        let files = this.state.files;

        let formData = new FormData();

        //Adding files to the formdata
        formData.append("image", files);
        formData.append("name", "Name");

        axios({
            // Endpoint to send files
            url: "http://localhost:8080/files",
            method: "POST",
            headers: {
                // Add any auth token here
                authorization: "your token comes here",
            },
            // Attaching the form data
            data: formData,
        })
            .then((res) => { }) // Handle the response from backend here
            .catch((err) => { }); // Catch errors if any
    }

    render() {
        return (
            <div>
                <h1>Select your files</h1>
                <input
                    type="file"
                    multiple="multiple" //To select multiple files
                    onChange={(e) => this.handleFile(e)}
                />
                <button onClick={(e) => this.handleUpload(e)}
                >Send Files</button>
            </div>
        );
    }
}

export default UploadFile;
