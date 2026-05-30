import os
import re

# The updated footer HTML content
NEW_FOOTER = """<footer class="bg-gray-900 text-white">
    <!-- Main Footer -->
    <div class="container mx-auto px-4 py-16">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8">
        <!-- Company Info -->
        <div class="lg:col-span-2">
          <img src="https://theworkmatch.com/img/WorkMatch_Logo.png" alt="WorkMatch" class="h-10 mb-4">
          <p class="text-gray-400 text-sm leading-relaxed mb-4">
            WorkMatch is a technology services company helping businesses move faster through digital engineering, cloud transformation, and IT talent solutions.
          </p>
          <!-- Address -->
          <div class="flex items-start gap-3 mb-4">
            <span class="mt-0.5 w-7 h-7 rounded-lg bg-gray-800 flex items-center justify-center flex-shrink-0">
              <i class="fas fa-location-dot text-blue-400 text-xs"></i>
            </span>
            <p class="text-gray-400 text-sm leading-relaxed">
              The Work Match, Old No 178/B1, New No 766/1,<br>
              Shakthi Towers 1, Thousand Lights,<br>
              Annasalai, Chennai - 600 002
            </p>
          </div>
          <!-- Contact -->
          <div class="flex flex-col gap-2 mb-6">
            <div class="flex items-center gap-3">
              <span class="w-7 h-7 rounded-lg bg-gray-800 flex items-center justify-center flex-shrink-0">
                <i class="fas fa-envelope text-blue-400 text-xs"></i>
              </span>
              <a href="mailto:info@theworkmatch.com" class="text-gray-400 hover:text-white transition-colors text-sm break-all">info@theworkmatch.com</a>
            </div>
            <div class="flex items-center gap-3">
              <span class="w-7 h-7 rounded-lg bg-gray-800 flex items-center justify-center flex-shrink-0">
                <i class="fas fa-phone text-blue-400 text-xs"></i>
              </span>
              <div class="flex flex-wrap gap-x-3 gap-y-1 text-sm">
                <a href="tel:+919176351712" class="text-gray-400 hover:text-white transition-colors">+91 91763 51712</a>
                <span class="text-gray-600">|</span>
                <a href="tel:+919344051712" class="text-gray-400 hover:text-white transition-colors">+91 93440 51712</a>
              </div>
            </div>
          </div>
          <!-- Social -->
          <div class="flex space-x-3">
            <a href="https://x.com/theworkmatch" class="w-9 h-9 bg-gray-800 rounded-lg flex items-center justify-center hover:bg-primary transition-colors">
              <i class="fab fa-twitter text-sm"></i>
            </a>
            <a href="https://www.linkedin.com/company/theworkmatch/about/?viewAsMember=true" class="w-9 h-9 bg-gray-800 rounded-lg flex items-center justify-center hover:bg-primary transition-colors">
              <i class="fab fa-linkedin-in text-sm"></i>
            </a>
          </div>
        </div>

        <!-- Services -->
        <div>
          <h3 class="text-lg font-semibold mb-6">Services</h3>
          <ul class="space-y-3">
            <li><a href="talent-solutions.html" class="text-gray-400 hover:text-white transition-colors">Talent Solutions</a></li>
            <li><a href="custom-software-engineering.html" class="text-gray-400 hover:text-white transition-colors">Custom Software Engineering</a></li>
            <li><a href="cloud-solutions.html" class="text-gray-400 hover:text-white transition-colors">Cloud Solutions</a></li>
            <li><a href="data-ai-solutions.html" class="text-gray-400 hover:text-white transition-colors">Data & AI Solutions</a></li>
            <li><a href="cms-solutions.html" class="text-gray-400 hover:text-white transition-colors">CMS Solutions</a></li>
            <li><a href="accounting-as-a-service.html" class="text-gray-400 hover:text-white transition-colors"> Accounting as a Service</a></li>
          </ul>
        </div>

        <!-- Company -->
        <div>
          <h3 class="text-lg font-semibold mb-6">Company</h3>
          <ul class="space-y-3">
            <li><a href="company-overview.html" class="text-gray-400 hover:text-white transition-colors">Company Overview</a></li>
            <li><a href="careers.html" class="text-gray-400 hover:text-white transition-colors">Careers</a></li>
            <li><a href="hire-talent.html" class="text-gray-400 hover:text-white transition-colors">Hire Talent</a></li>
            <li><a href="contact.html" class="text-gray-400 hover:text-white transition-colors">Contact Us</a></li>
          </ul>
        </div>

        <!-- Industries -->
        <div>
          <h3 class="text-lg font-semibold mb-6">Industries</h3>
          <ul class="space-y-3">
            <li><a href="bfsi.html" class="text-gray-400 hover:text-white transition-colors">BFSI</a></li>
            <li><a href="healthcare.html" class="text-gray-400 hover:text-white transition-colors">Healthcare</a></li>
            <li><a href="retail-ecommerce.html" class="text-gray-400 hover:text-white transition-colors">Retail & E-commerce</a></li>
            <li><a href="manufacturing.html" class="text-gray-400 hover:text-white transition-colors">Manufacturing</a></li>
            <li><a href="saas-startups.html" class="text-gray-400 hover:text-white transition-colors">SaaS & Startups</a></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Copyright -->
    <div class="border-t border-gray-800">
      <div class="container mx-auto px-4 py-6">
        <div class="text-center">
          <p class="text-gray-400">
            Copyright <i class="far fa-copyright"></i> 2026
            <a href="index.html" class="text-white hover:text-primary transition-colors">WorkMatch</a>.
            All Rights Reserved.
          </p>
        </div>
      </div>
    </div>
  </footer>"""

def update_footers():
    # Regex to find everything between <footer...> and </footer>
    footer_pattern = re.compile(r'<footer.*?>.*?</footer>', re.DOTALL)
    
    # Get all html files in the current directory
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if a footer exists
        if footer_pattern.search(content):
            new_content = footer_pattern.sub(NEW_FOOTER, content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Updated footer in: {file_path}")
        else:
            print(f"⚠️ No footer tag found in: {file_path}")

if __name__ == "__main__":
    update_footers()
