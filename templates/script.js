const githubButton =
    document.getElementById("githubButton");


githubButton.addEventListener(
    "click",
    function (event) {

        event.preventDefault();

        window.open(
            "https://github.com/mitulhadiya/DeepStacking",
            "_blank"
        );

    }
);

const sections =
    document.querySelectorAll(".section");


const observer =
    new IntersectionObserver(
        function (entries) {

            entries.forEach(
                function (entry) {

                    if (entry.isIntersecting) {

                        entry.target.style.opacity = "1";

                        entry.target.style.transform =
                            "translateY(0)";

                    }

                }
            );

        },
        {
            threshold: 0.1
        }
    );


sections.forEach(
    function (section) {

        section.style.opacity = "0";

        section.style.transform =
            "translateY(15px)";

        section.style.transition =
            "opacity 0.5s ease, transform 0.5s ease";

        observer.observe(section);

    }
);