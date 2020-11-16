from collab.core.models import Document


document_body = """
<p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi quis facilisis diam. Curabitur porta, leo vel viverra
    viverra, sem urna gravida libero, congue pretium mauris nibh non ex. Integer eu sapien et ligula ultricies porta ut
    vitae sapien. Vestibulum fringilla sem sit amet lorem euismod, in vehicula purus iaculis. Etiam ut elit blandit,
    sagittis tellus ut, bibendum sem. Donec id tortor sed ante vestibulum consequat. Nunc sed porttitor orci. Morbi
    dignissim nisi eu tellus venenatis, <span class="highlight">nec fermentum enim porta</span>
    </p>
    <p>
      Nam vel elit ipsum. Pellentesque posuere erat eget elit gravida, vel consequat metus rutrum. Vivamus ultricies justo
      eget semper auctor. Proin sit amet ante lectus. Nullam bibendum placerat leo, finibus egestas lacus sollicitudin
      sed.
      Maecenas vitae cursus libero, eu placerat ipsum. Suspendisse a velit blandit, fringilla est eu, convallis quam.
      Praesent non mauris id nibh sollicitudin congue. Maecenas vitae dignissim libero. Phasellus feugiat mauris purus,
      vel
      dictum nulla blandit et. Pellentesque iaculis condimentum lacus, eu vulputate ex efficitur sit amet. Sed convallis
      dictum diam at ullamcorper. Donec pretium erat non semper aliquet.
    </p>
    <p>
      Cras eu ipsum a mi blandit convallis. Nulla molestie augue ex, et luctus purus molestie nec. Ut id pellentesque
      ligula. Sed mollis tempus arcu. Praesent nec nunc pellentesque nibh vulputate rutrum. Proin quis auctor urna. Donec
      placerat fermentum euismod. Cras at mollis elit. Nam a nulla et lectus volutpat dignissim ut fermentum ex. Curabitur
      eleifend eu massa at sagittis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent ut est nulla.
      Etiam vel urna efficitur, semper enim a, molestie metus. Curabitur at velit vel metus fermentum fermentum non vitae
      magna. Quisque dapibus eu massa et eleifend. Sed pulvinar ligula at nunc dignissim, porttitor varius purus
      vulputate.
    </p>
    <p>
      Curabitur in interdum neque. Vivamus vulputate, nunc non hendrerit porttitor, sem sem rhoncus tellus, elementum
      tincidunt purus magna sit amet arcu. Integer luctus feugiat dui, et lacinia arcu rhoncus in. Mauris blandit nibh ac
      quam venenatis, id molestie ex rhoncus. Sed vitae eleifend ex. Fusce maximus sem vitae sem tempus accumsan. Praesent
      auctor vehicula sagittis. Proin ut molestie sem, ut viverra velit. Maecenas quis nulla pellentesque, auctor metus
      in,
      consectetur enim. Aenean ultricies purus a mi faucibus, in sollicitudin diam vestibulum. Nullam sagittis pulvinar
      metus, sollicitudin ultricies nibh condimentum ac.
    </p>
    <p>
      Sed venenatis, erat eu ultrices vulputate, ante mi posuere enim, ut imperdiet lectus metus ac dui. Cras odio magna,
      pulvinar quis magna ac, molestie varius arcu. Quisque posuere sit amet orci ut ultrices. Morbi malesuada nulla
      velit,
      eu hendrerit justo iaculis et. Vestibulum sed diam quis eros vehicula rhoncus. Vestibulum eu varius nibh. Praesent
      suscipit suscipit odio nec imperdiet. Duis aliquet, orci ut sagittis dapibus, nibh justo interdum augue, in laoreet
      enim libero placerat leo. Sed lacinia libero orci, eget tristique mauris porta tincidunt. Etiam vel facilisis neque.
      Integer vulputate congue augue ac euismod. Pellentesque magna metus, aliquam ac velit non, tristique ultricies
      tortor.
      Mauris sed elementum nisl.
    </p>
"""
def run():
    Document.objects.create(body=document_body)
