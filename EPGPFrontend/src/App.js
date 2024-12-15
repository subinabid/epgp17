import React, { useEffect, useState } from "react";
import Papa from "papaparse"; // For parsing CSV
import "./App.css";

function App() {
  const [profiles, setProfiles] = useState([]);

  useEffect(() => {
    // Load the CSV file
    fetch("/directory.csv")
      .then((response) => response.text())
      .then((data) => {
        Papa.parse(data, {
          header: true,
          skipEmptyLines: true,
          complete: (results) => {
            setProfiles(results.data);
          },
        });
      });
  }, []);

  return (
    <div className="container my-5">
      <h1 className="text-center mb-4">IIMK EPGP 17</h1>
      <div className="row gy-4">
        {profiles.map((profile, index) => (
          <div className="col-sm-12 col-md-6 col-lg-4" key={index}>
            <div className="card w-100">
              <div className="row">
                <div className="col-4"> 
                  <img
                  src={profile.ProfileImage?.trim() || "https://via.placeholder.com/150"}
                  className="card-img-top"
                  alt={profile.Name}
                  />
                </div>

                <div className="col-8">
                  <div className="card-body text-center">
                    <h5 className="card-title">{profile.Name}</h5>
                    <p className="card-text"> {profile.Employer}</p>
                    <p className="card-text">Batch: {profile.Batch} | Roll No: {profile.RollNumber}</p>
                    <p className="card-text">Phone: {profile.PhoneNumber}</p>
                    <p className="card-text">DoB: {profile.DOB}</p>
                    <p>

                      {profile.LinkedIn && (
                        <a
                        href={profile.LinkedIn}
                        target="_blank"
                        rel="noreferrer"
                        className="btn btn-primary btn-sm me-2"
                      >
                        LinkedIn
                      </a>
                      )}

                      {profile.Insta && (
                        <a
                          href={"https://www.instagram.com/" + profile.Insta + "/"}
                          target="_blank"
                          rel="noreferrer"
                          className="btn btn-secondary btn-sm"
                        >
                          Instagram
                        </a>
                      )}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;