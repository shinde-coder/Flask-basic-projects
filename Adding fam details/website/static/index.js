// function deleteFamilyMember(memberId) {
//     fetch("/delete-family-member", {
//       method: "POST",
//       body: JSON.stringify({ memberId: memberId }),
//     }).then((_res) => {
//       window.location.href = "/";
//     });
//   }

// function deleteFamilyMember(memberId) {
//   fetch("/delete-family-member", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({ memberId: memberId }),
//   })
//   .then((_res) => {
//     window.location.href = "/"; // Redirect to the home page after successful deletion
//   })
//   .catch((error) => {
//     console.error("Error deleting family member:", error);
//     // Handle any errors that occur during the deletion process, if needed
//   });
// }
