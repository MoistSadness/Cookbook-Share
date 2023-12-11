import Navbar from "./components/Navbar"
import Page from "./components/Page"
import Footer from "./components/Footer"

export default function App() {

  return (
    <body>
      <Navbar />
      <div className="container">
        <Page />
      </div>
      <Footer />
    </body>
  )
}